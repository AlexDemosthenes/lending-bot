# Task Manager App

A beautiful, modern task management application built with React, TypeScript, and Vite.

## Features

- **Create Tasks**: Add tasks with titles, descriptions, and priority levels (low, medium, high)
- **Mark as Complete**: Check off tasks as you complete them
- **Edit Tasks**: Inline editing of task details
- **Delete Tasks**: Remove tasks you no longer need
- **Priority Levels**: Organize tasks by priority with color-coded badges
- **Statistics Dashboard**: Track total, pending, and completed tasks
- **Persistent Storage**: Tasks are saved to browser's local storage
- **Responsive Design**: Beautiful UI that works on desktop and mobile devices
- **Modern UI/UX**: Gradient backgrounds, smooth animations, and intuitive interactions

## Tech Stack

- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe code
- **Vite**: Lightning-fast build tool and dev server
- **CSS3**: Modern styling with gradients and animations
- **Local Storage API**: Client-side data persistence

## Getting Started

### Prerequisites

- Node.js 16+ and npm installed

### Installation

1. Navigate to the task-app directory:
```bash
cd task-app
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and visit `http://localhost:3000`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint

## Usage

1. **Add a Task**: Fill in the task title, optional description, select priority, and click "Add Task"
2. **Complete a Task**: Click the checkbox next to a task to mark it as complete
3. **Edit a Task**: Click the edit (✏️) button to modify task details
4. **Delete a Task**: Click the delete (🗑️) button to remove a task
5. **View Statistics**: See your task statistics at the top of the page

## Project Structure

```
task-app/
├── src/
│   ├── components/
│   │   ├── Header.tsx/css       # Statistics dashboard
│   │   ├── TaskForm.tsx/css     # Form to add new tasks
│   │   ├── TaskList.tsx/css     # Container for task items
│   │   └── TaskItem.tsx/css     # Individual task component
│   ├── App.tsx/css              # Main application component
│   ├── main.tsx                 # Application entry point
│   └── index.css                # Global styles
├── index.html                   # HTML template
├── package.json                 # Dependencies and scripts
├── tsconfig.json                # TypeScript configuration
└── vite.config.ts              # Vite configuration
```

## Features in Detail

### Task Management
- Create tasks with meaningful titles and descriptions
- Set priority levels to organize your work
- Edit tasks inline without page navigation
- Delete tasks with a single click

### Visual Feedback
- Color-coded priority badges (low: blue-green, medium: orange-blue, high: pink-red)
- Smooth hover effects and transitions
- Completed tasks are visually distinguished with strikethrough text
- Responsive design that adapts to any screen size

### Data Persistence
- All tasks are automatically saved to browser's local storage
- Tasks persist across browser sessions
- No backend required - works entirely in the browser

## Browser Support

Works in all modern browsers that support:
- ES2020
- CSS Grid
- CSS Custom Properties
- Local Storage API

## License

MIT License - feel free to use this project for learning or as a starting point for your own applications.
