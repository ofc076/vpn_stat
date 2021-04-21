async function getData(url = '') {
  try {
  const response = await fetch(url, {
    cache: 'no-cache',
  }); 
  return await response.text(); 
  } catch (error) {
    console.log(`fail from ${url}`)
    return ''
  }
}

function checkAllLink() {
  const list = document.querySelectorAll('.dload-link')
  //const urls = Array.from(list).map(i => i.href)
  list.forEach(checkNewTask)

}

function checkNewTask(item) {
  const link = item.href;
    getData(link).then((text) => {
      if (text.search('404') == -1) {
        item.classList.add('text-danger', 'font-weight-bold');
      }
    })
}

document.addEventListener('DOMContentLoaded', checkAllLink)