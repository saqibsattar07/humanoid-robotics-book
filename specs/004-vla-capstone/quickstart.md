# Quickstart: Running the Book Locally

This guide provides instructions for setting up the Docusaurus environment to build and view the book locally.

## Prerequisites

- [Node.js](https://nodejs.org/) (version 18.0 or higher)
- [npm](https://www.npmjs.com/) (usually comes with Node.js) or [Yarn](https://yarnpkg.com/)

## 1. Install Dependencies

Navigate to the project's root directory and install the necessary dependencies defined in `package.json`.

**Using npm:**
```bash
npm install
```

**Using Yarn:**
```bash
yarn install
```

## 2. Start the Development Server

Once the dependencies are installed, you can start the Docusaurus development server. This will build the site and open it in your default web browser. The server will automatically rebuild the site and refresh the browser when you make changes to the content.

**Using npm:**
```bash
npm start
```

**Using Yarn:**
```bash
yarn start
```

By default, the site will be available at `http://localhost:3000`.

## 3. Project Structure for Content

The book's content is located in the `src/docs` directory. Each subdirectory represents a module, and the Markdown files within are the chapters.

```
src/
└── docs/
    ├── 001-ros2-nervous-system/
    │   └── ...
    ├── 002-digital-twin-simulation/
    │   └── ...
    ├── 003-isaac-robot-brain/
    │   └── ...
    └── 004-vla-capstone/
        ├── _category_.json
        ├── 01-voice-to-action.md
        ├── 02-cognitive-planning.md
        └── 03-capstone-overview.md
```

You can edit these Markdown files to see the changes reflected live in the browser.
