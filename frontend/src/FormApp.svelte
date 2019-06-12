<script>
    import { createEventDispatcher } from 'svelte';
    import { onMount } from 'svelte';

	const dispatch = createEventDispatcher();

	let subject = '';
	let message = '';
    let adverts = '';

	$: test = subject + " " + message;

	function sendForm() {
	    dispatch('formMess', {
			subject: subject + " Test!",
			message: message + "!!!"
		});
	}
	onMount(async () => {
		const res = await fetch(`http://127.0.0.1:8000/`);
        let text = await res.json();
        adverts = text.results
	});

</script>

<style>

</style>

<form>
    <input type="text" name="subject" bind:value={subject}>
    <input type="text" name="message" bind:value={message}>
    <button type="button" on:click="{sendForm}">Send</button>
</form>

	{#each adverts as advert}
		<p>{advert.subject}</p>
	{:else}
		<p>loading...</p>
	{/each}

<p>{subject}</p>
<p>{test}</p>
