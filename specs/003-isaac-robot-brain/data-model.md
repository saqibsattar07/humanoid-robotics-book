# Data Model for Book Content

This document defines the data structure for the book's content, which is stored in Markdown files formatted for Docusaurus.

## Chapter File Structure

Each chapter is a standalone `.md` file. The content should follow a logical flow with clear headings, explanations, code snippets, and diagrams.

## Frontmatter (Metadata)

Each Markdown file MUST include a Docusaurus frontmatter block at the top. This metadata is used for navigation, titling, and SEO.

```yaml
---
id: [unique-id]
title: "[Chapter Title]"
sidebar_label: "[Short Label for Sidebar]"
sidebar_position: [number]
tags: [tag1, tag2, tag3]
---
```

### Fields

- **`id`**: A unique identifier for the page. Convention is to use the filename without the extension.
- **`title`**: The main title of the chapter, displayed at the top of the page.
- **`sidebar_label`**: The short name for the chapter that appears in the sidebar navigation. If not provided, `title` is used.
- **`sidebar_position`**: A number that determines the order of the chapter in the sidebar.
- **`tags`**: A list of keywords related to the chapter's content, used for search and filtering.

## Module Category File

Each module (directory of chapters) should contain a `_category_.json` file to define its properties in the sidebar.

```json
{
  "label": "Module Name",
  "position": 3,
  "link": {
    "type": "generated-index",
    "description": "An overview of the chapters in this module."
  }
}
```

### Fields

- **`label`**: The name of the module displayed in the sidebar.
- **`position`**: The order of the module in the sidebar relative to other modules.
- **`link`**: Defines the behavior of the module category link itself. `generated-index` will create a page with links to all chapters in the module.
