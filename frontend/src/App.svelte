<script>
    import FormApp from './FormApp.svelte'
    import {count} from './store'

    let subjectTwo = '';
	let messageTwo = '';
    let count_value;

	function print(event) {
	    subjectTwo = event.detail.subject;
	    messageTwo = event.detail.message;
	}

	function increment() {
		count.update(n => n + 1);
	}

	const unsubscribe = count.subscribe(value => {
		count_value = value;
	});
</script>

<style>

</style>

<FormApp on:formMess="{print}"/>

<hr>
<h2>{subjectTwo}</h2>
<p>{messageTwo}</p>
<hr>
<button on:click={increment}>
	+
</button>

<p>Count = {$count}</p>