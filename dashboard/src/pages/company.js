import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import api from "@/services/api";
import { Chart } from "react-google-charts";
import Modal from "react-modal";
import Speech from "@/components/Speech";

export default function Company() {
  const router = useRouter();
  const { id } = router.query;
  const [company, setCompany] = useState([]);
  const [companyAnalysis, setCompanyAnalysis] = useState([]);
  const [filterValue, setFilterValue] = useState(new Date().getDate());
  const [filterType, setFilterType] = useState('day');
  const [formattedCompanyAnalysis, setFormattedCompanyAnalysis] = useState([]);
  const [isOpen, setIsOpen] = useState(false)

  const chartOptions = {
    chart: {
      title: "Histórico de notas",
      subtitle: "por tempo",
    },
  };

  const getCompanyAnalysis = async (
    companyID,
    valueFilter = new Date().getDate(),
    typeFilter = "day"
  ) => {
    let headers = {
      "value-filter": valueFilter,
      "type-filter": typeFilter,
      "company-id": companyID,
    };

    try {
      const response = await api.get("/sentimentAnalysis", { headers: headers });
      setCompanyAnalysis(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  function refreshData() {
    api.get(`/company/${id}`)
      .then((result) => {
        setCompany(result.data);
        getCompanyAnalysis(id);
      })
      .catch((error) => {
        console.error(error);
      });
  }

  useEffect(() => {
    console.log("Company ID " + id);
    refreshData();
  }, [id]);

  useEffect(() => {
    // Update chart data if companyAnalysis updated
    const formattedCompanyAnalysis = convertData(companyAnalysis);
    setFormattedCompanyAnalysis(formattedCompanyAnalysis);
  }, [companyAnalysis]);

  function convertData(data) {
    let formattedData = [["Data", company.name]];
    if (data.length == 0) formattedData = [];
    data.forEach((element) => {
      formattedData.push([element.date, element.grade]);
    });
    return formattedData;
  }

  const handleFormSubmit = (event) => {
    event.preventDefault();
    getCompanyAnalysis(id, filterValue, filterType);
    console.log('Dados do gráfico: ');
    console.log(formattedCompanyAnalysis);
  };

  return (
    <div className="flex h-full flex-col justify-center items-center">
      <h1 className="text-3xl mb-5 font-bold">{company.name}</h1>
      <h2 className="text-4xl">Nota atual: {(company.grade * 1).toFixed(2)}</h2>
      <div className="form-filter">
        <form onSubmit={handleFormSubmit}>
          <label htmlFor="value">Valor:</label>
          <input
            type="number"
            min="0"
            id="value"
            name="value"
            value={filterValue}
            onChange={(event) => setFilterValue(event.target.value)}
          />
          <label htmlFor="type">Tipo:</label>
          <select
            name="type"
            id="type"
            value={filterType}
            onChange={(event) => setFilterType(event.target.value)}
          >
            <option value="day">Dia</option>
            <option value="month">Mês</option>
            <option value="year">Ano</option>
          </select>
          <button type="submit">Filtrar</button>
        </form>
      </div>
      <div className="chart mt-5">
        {
          formattedCompanyAnalysis.length ?
            <Chart
              chartType="Line"
              width="100%"
              height="100%"
              data={formattedCompanyAnalysis}
              options={chartOptions}
            />
            :
            <h2>Nenhum dado encontrado!</h2>
        }
      </div>

      <button className="simulate-button" onClick={() => setIsOpen(true)}>Simular</button>

      <Modal className="simulation-modal" isOpen={isOpen} onRequestClose={() => setIsOpen(false)}>
        <button className="close-modal" onClick={() => setIsOpen(false)}>X</button>
        
        <Speech id={id} refreshData={refreshData} setIsOpen={setIsOpen} />

      </Modal>

    </div>
  );
}