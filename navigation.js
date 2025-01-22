async function generateMenu() {
    try {
        const response = await fetch('/site-structure.json');
        if (!response.ok) throw new Error('Failed to fetch site structure');

        const siteStructure = await response.json();

        // Create the burger menu container
        const nav = document.createElement('nav');
        const burger = document.createElement('div');
        burger.classList.add('burger');
        burger.innerHTML = '&#9776;'; // Burger icon

        const menu = document.createElement('ul');
        menu.classList.add('menu');

        // Generate the menu items
        for (const [section, links] of Object.entries(siteStructure)) {
            const sectionLi = document.createElement('li');
            sectionLi.textContent = section;

            const subsectionUl = document.createElement('ul');
            links.forEach(link => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                // Use an absolute path to prevent doubling
                a.href = link.url.startsWith('/')
                    ? `${window.location.origin}${link.url}`
                    : new URL(link.url, window.location.origin).href;
                a.textContent = link.name;
                li.appendChild(a);
                subsectionUl.appendChild(li);
            });

            sectionLi.appendChild(subsectionUl);
            menu.appendChild(sectionLi);
        }

        // Toggle menu visibility on burger click
        burger.addEventListener('click', () => {
            menu.classList.toggle('active');
        });

        nav.appendChild(burger);
        nav.appendChild(menu);
        document.body.insertBefore(nav, document.body.firstChild);
    } catch (error) {
        console.error('Error generating menu:', error);
    }
}

document.addEventListener('DOMContentLoaded', generateMenu);






  