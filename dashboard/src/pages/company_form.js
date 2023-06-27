import { useState } from "react";
import api from "@/services/api";

export default function CompanyForm({getCompanies}) {
  const [companyName, setCompanyName] = useState('');
  const [companyVisibility, setCompanyVisibility] = useState(true);

  const createCompany = async () => {
    let payload = {
      name: companyName,
      visibility: companyVisibility
    };

    try {
      const response = await api.post("/company", payload, );
      getCompanies();
      alert('Nova empresa cadastrada!');
    } catch (error) {
      console.error(error);
    }
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    createCompany();
  };

  return (
    <div className='flex h-full flex-col justify-center items-center'>
      <h1 className='text-4xl mb-5 font-bold'>Cadastro de empresa</h1>
      <div className="form-new-company">
        <form onSubmit={handleFormSubmit}>
          <div className="form-item">
            <input
              type="text"
              id="name"
              name="name"
              placeholder="Nome da empresa"
              value={companyName}
              onChange={(event) => setCompanyName(event.target.value)}
            />
          </div>
          <div className="form-item">
            <label htmlFor="visibility">Visibilidade:</label>
            <input 
              type="checkbox"
              id="visibility"
              checked={companyVisibility}
              onChange={(event) => setCompanyVisibility(event.target.value)}
            />
          </div>
          <button type="submit">Cadastrar</button>
        </form>
      </div>
    </div>
  );
}