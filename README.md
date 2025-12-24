# My Archival Site

A Hugo-powered static website for archiving documents, meeting minutes, and project materials.

## Setup Instructions

### 1. Clone and Initialize Theme

```bash
cd my-archivals
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke themes/ananke
git submodule init
git submodule update
```

### 2. Update Configuration

Edit `hugo.toml` and update:
- `baseURL` to match your GitHub Pages URL: `https://YOUR_USERNAME.github.io/YOUR_REPOSITORY_NAME`
- `title` and other site parameters as needed

### 3. Local Development

```bash
# Install Hugo (if not already installed)
brew install hugo

# Run local development server
hugo server -D

# Build for production
hugo --gc --minify
```

### 4. GitHub Pages Setup

1. Push this repository to GitHub
2. Go to repository Settings > Pages
3. Set Source to "GitHub Actions"
4. The site will automatically deploy when you push to the main branch

### 5. Adding Content

Create new posts:
```bash
hugo new posts/my-new-post.md
```

Create new pages:
```bash
hugo new about.md
```

## Directory Structure

```
my-archivals/
├── content/           # Markdown content files
│   ├── posts/        # Blog posts
│   └── _index.md     # Homepage content
├── themes/           # Hugo themes
├── static/           # Static assets (images, CSS, JS)
├── layouts/          # Custom layout templates
├── .github/workflows/ # GitHub Actions for deployment
└── hugo.toml         # Site configuration
```

## Features

- Responsive design with Ananke theme
- Automatic deployment to GitHub Pages
- Fast static site generation
- SEO-friendly URLs
- Tag and category support