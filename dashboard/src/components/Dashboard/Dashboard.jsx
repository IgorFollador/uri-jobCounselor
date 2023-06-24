import { useState } from 'react';
import { useRouter } from 'next/router'
import Image from 'next/image'
import Link from 'next/link'
import Logo from '@/../public/assets/logo.png'
import api from "../../services/api";

export default function Dashboard({ children }) {
    const router = useRouter();
    const [companies, setCompanies] = useState([]);

    const getCompanies = async () => {
        await api.get("/companies")
        .then(result => {
            console.log(result.data);
            setCompanies(result.data);
        })
    }
    
    getCompanies();

    const menuItems = [
        {
            href: '/',
            name: 'Homepage',
        },
        {
            href: '/amazon',
            name: 'Amazon Company',
        },
    ]

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
                        {companies.map(({ name}) => (
                            <li className='m-2' key={name}>
                                <Link 
                                    href={name}
                                    className={`flex p-2 bg-orange-200 rounded hover:bg-orange-500 hover:text-white cursor-pointer 
                                    ${router.asPath === name && 'bg-fuchsia-text-white'}`}
                                >
                                    {name}
                                </Link>
                            </li>
                        ))}
                        </ul>
                    </nav>
                </aside>
                <main className='flex-1'>{children}</main>
            </div>
        </div>
    )
}