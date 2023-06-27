import { useEffect } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import Logo from '@/../public/assets/logo.png'

export default function Dashboard({ children, getCompanies, companies }) {
    useEffect(() => {
        getCompanies();
    }, []);

    return (
        <div className='min-h-screen flex flex-col'>
            <header className='sticky top-0 flex justify-center items-center bg-slate-200'>
                <Image 
                    src={Logo}
                    height={175}
                    alt="Job Counselor Logo"
                />
            </header>
            <div className='flex flex-col md:flex-row flex-1'>
                <aside className='bg-slate-200 w-full md:w-60'>
                    <nav>
                        <ul>
                            <li className='m-2'>
                                <Link 
                                    href={'/'}
                                    className={`flex p-2 bg-orange-200 rounded hover:bg-orange-500 hover:text-white cursor-pointer`}
                                >
                                    Homepage
                                </Link>
                            </li>

                            <li className='m-2'><span>Empresas:</span></li>
                        {companies.map((company) => (
                            company.visibility &&
                            <li className='m-2' key={company.name}>
                                <Link 
                                    href={{
                                        pathname: `/company`,
                                        query: {
                                            id: company.id,
                                        },
                                    }}
                                    // as={`/company/${company.name.toLowerCase()}`}
                                    className={`flex p-2 bg-orange-200 rounded hover:bg-orange-500 hover:text-white cursor-pointer`}
                                >
                                    {company.name}
                                </Link>
                            </li>
                        ))}
                            <li className='m-2'>
                                <Link 
                                    href={'/company_form'}
                                    className={`flex p-2 bg-green-300 rounded hover:bg-green-500 hover:text-white cursor-pointer`}
                                >
                                    Criar empresa
                                </Link>
                            </li>
                        </ul>
                    </nav>
                </aside>
                <main className='flex-1'>{children}</main>
            </div>
        </div>
    )
}