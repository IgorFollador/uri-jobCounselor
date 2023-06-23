import Dashboard from '@/components/Dashboard'
import '@/styles/globals.css'

export default function App({ Component, pageProps }) {
  return (
    <Dashboard>
      <Component {...pageProps} />
    </Dashboard>
  )
}
