let ans = document.getElementsByName('answer')

for (let i=0; ans.length > i; i++) {
    ans[i].addEventListener('click' ,function (e) {
        console.log(ans[i].value)
    })
}

// let subBtn = document.getElementById('form')
// subBtn.addEventListener('submit', function (e) {
//     console.log(answer)
// })

