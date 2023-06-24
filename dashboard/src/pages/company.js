import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import api from "@/services/api";
import { Chart } from "react-google-charts";

export default function Company() {
  const router = useRouter();
  const {id} = router.query;
  const [ company, setCompany ] = useState([]);
  const [ companyAnalysis, setCompanyAnalysis ] = useState([]);

  useEffect(() => {
    console.log('Company ID ' + id);
    api.get(`/company/${id}`)
    .then(result => {
        setCompany(result.data);
    });

    let headers = {
      'value-filter': 24,
      'type-filter': 'day',
      'company-id': id
    }

    api.get('/sentimentAnalysis', {headers: headers})
    .then(result => {
      setCompanyAnalysis(result.data);
    });
  }, [id]);

  // MOCKS
  const data = [
    [
      "Day",
      company.name
    ],
    ['2023-06-24 12:09:13', 7],
    ['2023-06-24 13:09:13', 8],
  ];
  
  const options = {
    chart: {
      title: "Histórico de notas",
      subtitle: "por tempo",
    },
  };

  return (
    <div className='flex h-full flex-col justify-center items-center'>
      <h1 className='text-3xl mb-5 font-bold'>{company.name}</h1>
      <h2 className="text-4xl">Nota atual: {(company.grade*100/100).toFixed(2)}</h2>
      <div className="chart mt-5 width">
        <Chart
          chartType="Line"
          width="100%"
          height="100%"
          data={data}
          options={options}
        />
      </div>

    </div>
  );
}