const form = document.getElementById("todoForm"); //document весь файл
const input = document.getElementById("taskInput"); //const значение
const list = document.getElementById("todoList"); 

form.addEventListener("submit", function (event) {
    event.preventDefault(); //нажимаеи add форма создается 

    const text = input.value.trim(); //текст из инпута 
    if (text === "") return;
    
    const li = document.createElement("li"); //строка списка
    
    const checkbox = document.createElement("input"); //чекбокс
    checkbox.type = "checkbox";
    
    const span = document.createElement("span"); //текст задачи
    span.textContent = text;
    
    const delBtn = document.createElement("button"); //кнопка удаления
    delBtn.textContent = "🗑";

    li.appendChild(checkbox); //по типу положить внутрь 
    li.appendChild(span);
    li.appendChild(delBtn);

    list.appendChild(li); //добавляем задачу в список

    input.value = ""; //чтобы после удаления текст исчезал

    checkbox.addEventListener("change", function () {
      if (checkbox.checked) {
        span.style.textDecoration = "line-through";
        span.style.opacity = "0.6";
      } else {
        span.style.textDecoration = "none";
        span.style.opacity = "1";
      }
    });

    delBtn.addEventListener("click", function () {
        list.removeChild(li);
    });
});




