let libItButton = document.querySelector("#lib-button");
libItButton.addEventListener("click", gatherAllInputsData);

function gatherAllInputsData() {
  let inputTypeText = document.querySelectorAll("input[type='text']");
  let inputArray = [];
  let emptyInput = false;
  inputTypeText.forEach((element) => {
    inputArray.push(element.value);
    if (element.value.trim() === "") {
      emptyInput = true;
    }
  });
  if (emptyInput) {
    // in case there are emptry inputs
    alert("please fill all boxes");
    return;
  }

  let storySpan = document.querySelector("#story");
  storySpan.textContent = inputArray.join(" ");
}
