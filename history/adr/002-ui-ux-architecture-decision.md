# ADR-002: UI/UX Architecture Decision for Docusaurus Book with RAG Chatbot

## Status
Accepted

## Date
2025-12-23

## Context
The Physical AI & Humanoid Robotics book requires a cohesive learning platform where the homepage, book pages, and embedded RAG chatbot feel like one consistent product. Students need a unified experience with minimal cognitive load while maintaining academic tone and professional appearance. The UI must follow accessibility standards while incorporating subtle animations that enhance clarity rather than distract.

## Decision
We will implement a unified UI/UX architecture consisting of:

- **Design System**: Tailwind CSS with shadcn/ui components and Framer Motion for animations, using the specified color palette (#4f8cff primary, #0b0f1a background, etc.) and typography (Inter, JetBrains Mono)
- **Homepage Layout**: Hero section with title/subtitle and "Start Learning" CTA that scrolls to 4-module card grid
- **Module Cards**: Clickable cards with hover animations (soft glow + slight lift) using shadcn Card components
- **Chatbot Integration**: Floating widget in bottom-right corner with consistent styling, message bubbles in primary blue (user) and dark indigo (bot), citations as mini cards
- **Animation Strategy**: Subtle Framer Motion animations that enhance clarity, including smooth open/close, typing indicators, and hover effects
- **Accessibility**: WCAG 2.1 AA compliance across all components

This approach ensures visual consistency while providing an engaging but focused learning experience.

## Consequences
### Positive
- Unified design language across all components creates cohesive product experience
- Consistent color palette and typography maintain professional academic appearance
- Subtle animations enhance user experience without distraction
- Accessible design ensures usability for all students
- Module cards provide clear navigation with intuitive hover feedback
- Floating chatbot feels native rather than embedded, improving user engagement
- Responsive design works across desktop, tablet, and mobile devices

### Negative
- Requires coordination between multiple UI libraries (Tailwind, shadcn/ui, Framer Motion)
- Animation performance needs careful optimization to maintain 60fps
- Accessibility compliance adds implementation complexity
- Maintaining visual consistency requires discipline across development team
- Design system setup has initial overhead before feature development

## Alternatives
### Alternative 1: Separate UI Systems
- Approach: Use different styling approaches for homepage vs chatbot
- Trade-offs: Would allow independent development but violate unified product requirement and create inconsistent user experience

### Alternative 2: Heavy Animation Approach
- Approach: Use extensive animations and transitions throughout the interface
- Trade-offs: More engaging visually but would distract from academic content and violate the "animations enhance clarity, not distraction" requirement

### Alternative 3: Marketing-Style Visuals
- Approach: Use colorful, marketing-focused design with promotional elements
- Trade-offs: More visually appealing but would not match academic tone and could distract from learning objectives

### Alternative 4: Minimal Interface
- Approach: Use extremely minimal interface with basic styling
- Trade-offs: Simpler to implement but would not meet production-ready appearance requirements and could feel unpolished

## References
- specs/001-rag-chatbot/spec.md
- specs/001-rag-chatbot/plan.md
- CLAUDE.md project instructions