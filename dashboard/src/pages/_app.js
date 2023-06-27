import Dashboard from '@/components/Dashboard'
import '@/styles/globals.css'
import { useState } from 'react';
import api from "@/services/api";

export default function App({ Component, pageProps }) {
  const [companies, setCompanies] = useState([]);

  const getCompanies = async () => {
    api.get("/companies")
    .then(result => {
        setCompanies(result.data);
    })
  }

  return (
    <Dashboard getCompanies={getCompanies} companies={companies} >
      <Component {...pageProps} getCompanies={getCompanies} />
    </Dashboard>
  )
}
