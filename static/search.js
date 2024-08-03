// document.getElementById('searchInput').addEventListener('input', function() {
//     const searchTerm = this.value.toLowerCase();
//     const profiles = document.getElementsByClassName('profile-item');
    
//     Array.from(profiles).forEach(function(profile) {
//         const name = profile.getElementsByTagName('h2')[0].textContent.toLowerCase();
//         const industryOrSpecialty = profile.getElementsByTagName('p')[0].textContent.toLowerCase();
        
//         if (name.includes(searchTerm) || industryOrSpecialty.includes(searchTerm)) {
//             profile.style.display = 'flex';
//         } else {
//             profile.style.display = 'none';
//         }
//     });
// });
