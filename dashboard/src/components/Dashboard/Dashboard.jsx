import { useRouter } from 'next/router'
import Image from 'next/image'
import Link from 'next/link'
import Logo from '@/../public/assets/logo.png'

export default function Dashboard({ children }) {
    const router = useRouter();

    const menuItems = [
        {
            href: '/',
            title: 'Homepage',
        },
        {
            href: '/amazon',
            title: 'Amazon Company',
        },
    ]

    return (
        <div className='min-h-screen flex flex-col'>
            <header className='sticky top-0 h-200 flex justify-center items-center bg-slate-200'>
                <Image 
                    src={Logo}
                    height={150}
                    alt="Job Counselor Logo"
                />
            </header>
            <div className='flex flex-col md:flex-row flex-1'>
                <aside className='bg-slate-200 w-full md:w-60'>
                    <nav>
                        <ul>
                        {menuItems.map(({ href, title }) => (
                            <li className='m-2' key={title}>
                                <Link 
                                    href={href}
                                    className={`flex p-2 bg-orange-200 rounded hover:bg-orange-500 hover:text-white cursor-pointer 
                                    ${router.asPath === href && 'bg-fuchsia-text-white'}`}
                                >
                                    {title}
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