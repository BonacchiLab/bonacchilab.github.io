# Computational, Cognitive, and Behavioral Neuroscience Lab (CCBN)

## Prerequisites

    - Python 3.12
    - uv package manager
    - Git

## Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/BonacchiLab/bonacchilab.github.io.git
   cd bonacchilab.github.io
   ```

2. Create a new Python environment using uv:

   ```bash
   uv venv
   ```

3. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`

4. Install dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

5. Start the development server:

   ```bash
   mkdocs serve
   ```

6. Open your browser and visit `http://127.0.0.1:8000`

## Running Tests

After installing dependencies, run the test suite with:

```bash
pytest
```

## Adding Content

1. Create new `.md` files in the `docs` directory
2. Update `mkdocs.yml` to include new pages in the navigation
3. Use Markdown syntax to write your content
4. The site will automatically reload when you save changes

## Deploying to GitHub Pages

1. Make sure your changes are committed and pushed to the main branch:

   ```bash
   git add .
   git commit -m "Update website content"
   git push origin main
   ```

2. Deploy to GitHub Pages using MkDocs:

   ```bash
   mkdocs gh-deploy
   ```

   This command will:
   - Build your documentation
   - Create a gh-pages branch (if it doesn't exist)
   - Push the built site to the gh-pages branch
   - The site will be available at `https://bonacchilab.github.io`

3. Verify the deployment:
   - Go to your repository's Settings > Pages
   - Ensure the source is set to "gh-pages" branch
   - Check that your site is published at the correct URL

## Best Practices

1. Always preview changes locally before deploying
2. Use meaningful commit messages
3. Keep the content up to date
4. Optimize images before uploading
5. Use consistent formatting across pages
