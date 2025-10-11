document.getElementById('new-prayer-btn').addEventListener('click', function() {
    fetch('/random-prayer')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById('prayer-container');
            container.innerHTML = `
                <div class="prayer-title">${data.title}</div>
                <div class="saint-attribution">— ${data.saint}</div>
                <div class="prayer">${data.prayer}</div>
                <button class="new-prayer-btn" id="new-prayer-btn">Show New Prayer</button>
                <div class="orthodox-cross">☦</div>
            `;
            // Re-attach event listener to the new button
            document.getElementById('new-prayer-btn').addEventListener('click', arguments.callee);
        })
        .catch(error => {
            console.error('Error fetching prayer:', error);
            alert('Failed to load a new prayer. Please try again.');
        });
});