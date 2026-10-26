export const profile = {
  name: 'Lisa Indraputri',
  title: 'Senior Software Development Engineer',
  line: 'Mobile web · Vue · Nuxt',
  email: 'lisaindraputri98@gmail.com',
  linkedin: 'https://www.linkedin.com/in/lisa-indraputri/',
}

export const experience = {
  company: 'DANA Indonesia',
  href: 'https://play.google.com/store/apps/details?id=id.dana',
  appStore: 'https://apps.apple.com/id/app/dana-dompet-digital-indonesia/id1437123008',
  range: 'Late 2019 – now',
  roles: [
    {
      title: 'Senior SDE',
      years: '2025 – now',
      current: true,
      details: [
        'Social: Feeds revamp, birthday feeds, and in-app chat with media, with a system analysis for each release',
        'Account Recovery end to end: change number with risk checks, transfer, merge, lost phone, and change number via link',
        'Real native error codes on all 4 recovery flows, and a conversion drop traced to network errors on the eligibility check',
        'TypeScript at zero errors across the app and its tests, with a 1,500+ Vitest suite kept green',
        'Design system implemented on 4 web apps, with visual-regression audits on each change',
        'Core Web Vitals on high-traffic recovery pages, and a repeatable Lighthouse setup',
        'AI-assisted tooling for CI, tickets, QA cases, and incident triage',
      ],
    },
    {
      title: 'SDE',
      years: '2022 – 2024',
      current: false,
      details: [
        'Front end for DANA Deals & Promotions and B2B, then promoted to Senior SDE',
        'Deals 2.0: voucher search, category pills, visual filters, recommendation sorting, and skeleton loading',
        'Buy as Gift end to end: themes, messages, birthday notifications, and back-office tools',
        'Growth: TikTok Live, a universal deeplink, targeted click-to-claim, and Google Ads attribution',
        'Seasonal campaign assets made configurable, so they no longer had to be swapped by hand',
        'B2B: role-based menus, enterprise-wallet cash-out approval, and a QoS dashboard',
        '25+ system analysis documents',
      ],
    },
    {
      title: 'Associate SDE',
      years: 'Dec 2019 – 2021',
      current: false,
      details: [
        'Online-to-offline and financial-service features, built to stay stable and maintainable',
        'Checked UI/UX designs for technical feasibility',
        'Learned the product, improved performance, and fixed defects',
        'Improved stability and the user experience',
        'Worked with the rest of the team',
      ],
    },
    {
      title: 'Front End Engineer Intern',
      years: '2019',
      current: false,
      details: [
        'Built the site from scratch in Vue and Laravel',
        'Improved performance through SEO',
        'Checked UI/UX designs for technical feasibility',
      ],
    },
  ],
}

export const skillsIntro =
  'Interfaces in Vue, Nuxt, and React. TypeScript and Tailwind to build them. Web Vitals, Sentry, and Mixpanel to keep them fast. AI tooling for the routine work around a release.'

export const skills = [
  'Vue',
  'Nuxt',
  'React',
  'TypeScript',
  'Tailwind',
  'Web Vitals',
  'Sentry',
  'Mixpanel',
  'Jira',
  'Notion',
  'AI tooling',
]

export const work = [
  {
    number: '01',
    title: 'Trip Craft',
    line: 'Shared trip planner.',
    details: [
      'Dates, places, flights, and stays',
      'One itinerary, with a join link',
      'A day plan suggested by Gemini',
    ],
    stack: 'Nuxt · Supabase',
    href: 'https://trip-craft-phi.vercel.app/',
  },
  {
    number: '02',
    title: 'STTAA Admissions',
    line: 'College admissions, live.',
    details: [
      'Admission waves for new students',
      'Registration forms and recommendations',
      'Application status and the registration payment',
    ],
    stack: 'Vue',
    href: 'https://admisi.sttaa.ac.id/',
  },
]
