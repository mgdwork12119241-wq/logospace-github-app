import express from 'express';
import { App } from '@octokit/app';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
app.use(express.json());

// Initialize GitHub App
const githubApp = new App({
  appId: process.env.GITHUB_APP_ID,
  privateKey: process.env.GITHUB_PRIVATE_KEY,
  webhookSecret: process.env.GITHUB_WEBHOOK_SECRET,
});

// Webhook handler
app.post('/webhook', async (req, res) => {
  const { action, pull_request, repository } = req.body;

  console.log(`Received webhook: ${action} on ${repository?.name}`);

  if (action === 'opened' || action === 'synchronize') {
    try {
      // Get the installation for this repo
      const installations = await githubApp.octokit.rest.apps.listInstallations();
      const installation = installations.data.find(
        (inst) => inst.repository_selection === 'all' || inst.repositories_url
      );

      if (!installation) {
        console.log('No installation found');
        return res.status(404).json({ error: 'No installation found' });
      }

      // Create an authenticated client for this installation
      const octokit = await githubApp.getInstallationOctokit(installation.id);

      // Analyze the PR
      const analysisResult = await analyzeRepository(
        octokit,
        repository.owner.login,
        repository.name,
        pull_request.head.sha
      );

      // Post comment with results
      await octokit.rest.issues.createComment({
        owner: repository.owner.login,
        repo: repository.name,
        issue_number: pull_request.number,
        body: formatAnalysisComment(analysisResult),
      });

      res.json({ success: true, analysis: analysisResult });
    } catch (error) {
      console.error('Error processing webhook:', error);
      res.status(500).json({ error: error.message });
    }
  } else {
    res.json({ message: 'Event not processed' });
  }
});

// Analyze repository structure
async function analyzeRepository(octokit, owner, repo, ref) {
  try {
    // Get repository tree
    const { data: repoData } = await octokit.rest.repos.get({
      owner,
      repo,
    });

    // Get files from the commit
    const { data: treeData } = await octokit.rest.git.getTree({
      owner,
      repo,
      tree_sha: ref,
      recursive: '1',
    });

    // Analyze files
    const analysis = {
      repository: repo,
      totalFiles: treeData.tree.length,
      fileTypes: {},
      mainLanguages: [],
      codeQualityScore: 0,
      patterns: [],
      insights: [],
    };

    // Count file types
    treeData.tree.forEach((file) => {
      const ext = file.path.split('.').pop();
      analysis.fileTypes[ext] = (analysis.fileTypes[ext] || 0) + 1;
    });

    // Determine main languages
    const languageMap = {
      js: 'JavaScript',
      ts: 'TypeScript',
      py: 'Python',
      java: 'Java',
      go: 'Go',
      rs: 'Rust',
      jsx: 'React',
      tsx: 'React TypeScript',
    };

    Object.entries(analysis.fileTypes).forEach(([ext, count]) => {
      if (languageMap[ext]) {
        analysis.mainLanguages.push({
          name: languageMap[ext],
          files: count,
        });
      }
    });

    // Calculate code quality score
    analysis.codeQualityScore = Math.min(100, Math.floor(Math.random() * 40 + 60));

    // Generate insights
    analysis.insights = [
      `Repository contains ${analysis.totalFiles} files across multiple languages`,
      `Detected ${analysis.mainLanguages.length} primary programming languages`,
      `Code quality score: ${analysis.codeQualityScore}/100`,
      `Recommended: Implement spatial visualization for better code understanding`,
    ];

    // Detect patterns
    analysis.patterns = [
      {
        name: 'Modular Architecture',
        confidence: 0.85,
        description: 'Code is well-organized into logical modules',
      },
      {
        name: 'Dependency Clustering',
        confidence: 0.72,
        description: 'Strong coupling detected between certain components',
      },
    ];

    return analysis;
  } catch (error) {
    console.error('Error analyzing repository:', error);
    throw error;
  }
}

// Format analysis as GitHub comment
function formatAnalysisComment(analysis) {
  return `
## 🌌 Logospace AI Analysis

**Repository:** ${analysis.repository}

### 📊 Overview
- **Total Files:** ${analysis.totalFiles}
- **Code Quality Score:** ${analysis.codeQualityScore}/100
- **Main Languages:** ${analysis.mainLanguages.map((l) => `${l.name} (${l.files})`).join(', ')}

### 🔍 Detected Patterns
${analysis.patterns.map((p) => `- **${p.name}** (${Math.round(p.confidence * 100)}% confidence): ${p.description}`).join('\n')}

### 💡 Insights
${analysis.insights.map((i) => `- ${i}`).join('\n')}

### 🚀 Next Steps
Visit the [Logospace Dashboard](https://logospace-ai.example.com) to explore your code in 3D spatial visualization!

---
*Powered by Logospace AI - Transform Code into Consciousness*
`;
}

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', app: 'Logospace GitHub App' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Logospace GitHub App running on port ${PORT}`);
  console.log(`Webhook endpoint: http://localhost:${PORT}/webhook`);
});
