import { useState } from 'react'
import './TaskForm.css'

interface TaskFormProps {
  onAddTask: (task: {
    title: string
    description: string
    completed: boolean
    priority: 'low' | 'medium' | 'high'
  }) => void
}

function TaskForm({ onAddTask }: TaskFormProps) {
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [priority, setPriority] = useState<'low' | 'medium' | 'high'>('medium')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!title.trim()) return

    onAddTask({
      title: title.trim(),
      description: description.trim(),
      completed: false,
      priority
    })

    setTitle('')
    setDescription('')
    setPriority('medium')
  }

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <h2 className="form-title">Add New Task</h2>
      
      <div className="form-group">
        <input
          type="text"
          className="form-input"
          placeholder="Task title..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          maxLength={100}
        />
      </div>

      <div className="form-group">
        <textarea
          className="form-textarea"
          placeholder="Task description (optional)..."
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          maxLength={500}
          rows={3}
        />
      </div>

      <div className="form-row">
        <div className="priority-group">
          <label className="priority-label">Priority:</label>
          <div className="priority-buttons">
            <button
              type="button"
              className={`priority-btn priority-low ${priority === 'low' ? 'active' : ''}`}
              onClick={() => setPriority('low')}
            >
              Low
            </button>
            <button
              type="button"
              className={`priority-btn priority-medium ${priority === 'medium' ? 'active' : ''}`}
              onClick={() => setPriority('medium')}
            >
              Medium
            </button>
            <button
              type="button"
              className={`priority-btn priority-high ${priority === 'high' ? 'active' : ''}`}
              onClick={() => setPriority('high')}
            >
              High
            </button>
          </div>
        </div>

        <button type="submit" className="submit-btn">
          <span className="btn-icon">+</span>
          Add Task
        </button>
      </div>
    </form>
  )
}

export default TaskForm
