import './Header.css'

interface HeaderProps {
  stats: {
    total: number
    completed: number
    pending: number
  }
}

function Header({ stats }: HeaderProps) {
  return (
    <div className="header">
      <h1 className="header-title">
        <span className="header-icon">✓</span>
        Task Manager
      </h1>
      <p className="header-subtitle">Stay organized and productive</p>
      <div className="stats">
        <div className="stat-card">
          <span className="stat-value">{stats.total}</span>
          <span className="stat-label">Total</span>
        </div>
        <div className="stat-card">
          <span className="stat-value">{stats.pending}</span>
          <span className="stat-label">Pending</span>
        </div>
        <div className="stat-card stat-card-success">
          <span className="stat-value">{stats.completed}</span>
          <span className="stat-label">Completed</span>
        </div>
      </div>
    </div>
  )
}

export default Header
