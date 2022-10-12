const getCookie = (name) => {
  let cookie

  if (document.cookie) {
    const cookies = document.cookie.split(";")

    for (let i in cookies) {
      cookies[i] = cookies[i].trim()

      if (cookies[i].substring(0, name.length + 1) === name + '=') {
        cookie = decodeURIComponent(cookies[i].substring(name.length + 1))
        break
      }
    }
  }

  return cookie
}

const createTodolistCard = (id, title, date, description, isFinished) => {
  const updateId = `update-status-${id}`
  const deleteId = `delete-task-${id}`

  return `
  <div class="task col">
    <h1 class="card-title task-title">${title}</td>
    <p class="card-subtitle task-details">${date}</td>
    <p class="card-text task-details">${description}</td>
    <p class="card-text task-details">
    ${isFinished ? "Finished" : "Not Finished"} 
    </p>
      <form id="${updateId}" onsubmit="updateTodolistStatus(event)" class="task-btn" method="POST">
        <input type="hidden" name="id" value="${id}"/>
        <button class="btn btn-primary" type="submit">Change Status</button>
      </form>
    <td>
      <form id="${deleteId}" onsubmit="deleteTodolistItem(event)" class="task-btn" method="POST" action="/todolist/delete-task/${id}">
        <input type="hidden" name="id" value="${id}"/>
        <button class="btn btn-primary" type="submit">Delete</button>
      </form>
    </td>
  </div>
  `
}

const updateTodolistStatus = async (event) => {
  event.preventDefault()

  const form = new FormData(event.target)
  const id = form.get("id")

  const csrfToken = getCookie('csrftoken')

  await fetch("/todolist/update-status/" + id, {
    method: 'POST',
    headers: {
      'X-CSRFTOKEN': csrfToken
    }
  })

  await renderTodolist()
}

const deleteTodolistItem = async (event) => {
  event.preventDefault()

  const form = new FormData(event.target)
  const id = form.get("id")

  const csrfToken = getCookie('csrftoken')

  await fetch("/todolist/delete-task/" + id, {
    method: 'DELETE',
    headers: {
      'X-CSRFTOKEN': csrfToken
    }
  })

  await renderTodolist()
}

const createTask = async (event) => {
  event.preventDefault()

  const form = new FormData(event.target)
  let data = {}

  form.forEach((value, key) => {
    data[key] = value
  })

  const csrfToken = getCookie('csrftoken')

  await fetch("/todolist/add", {
    method: 'POST',
    headers: {
      'X-CSRFTOKEN': csrfToken
    },
    body: JSON.stringify(data)
  })

  document.getElementById('closeTaskModal').click()

  await renderTodolist()
}

const renderTodolist = async () => {
  const res = await fetch("/todolist/json")
  const data = await res.json()

  let items = ``

  data.forEach(({ pk: id, fields }) => {
    const { title, date, description, is_finished } = fields

    items += createTodolistCard(id, title, date, description, is_finished)

  })

  document.getElementById('todolist').innerHTML = items
}

if (window.location.pathname === "/todolist/") {
  renderTodolist()
}
