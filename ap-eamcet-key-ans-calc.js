// copy paste below code in console
(() => {
	const questions = Array.from(document.querySelectorAll('.question-pnl'));
	let count = 0;
	console.log('Total no. of questions: ' + questions.length);
	questions.forEach(question => {
		const options = Array.from(question.querySelectorAll('.questionRowTbl tbody tr')).slice(3);
		const ans = options.findIndex(a => a.innerHTML.includes('rightAns')) + 1;
		const selected = parseInt(Array.from(question.querySelectorAll('.menu-tbl tr .bold'))[2].innerHTML);
		console.log('Ans: ' + ans + " Selected: " + selected);
		if (ans === selected) {
			count++;
		}
	});
	console.log('---------------- * -----------------')
	console.log("TOTAL: " + count);
})();