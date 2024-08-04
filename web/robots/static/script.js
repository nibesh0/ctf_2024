document.addEventListener('DOMContentLoaded', function() {
    const robots = [
        { name: 'Ultra Magnus', img: 'https://robohash.org/1' },
        { name: 'Optimus Prime', img: 'https://robohash.org/2' },
        { name: 'megatron', img: 'https://robohash.org/3' }
    ];

    const container = document.getElementById('robots-container');
    robots.forEach(robot => {
        const robotDiv = document.createElement('div');
        robotDiv.className = 'robot';
        robotDiv.innerHTML = `<img src="${robot.img}" alt="${robot.name}"><p>${robot.name}</p>`;
        container.appendChild(robotDiv);
    });
});
