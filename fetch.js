async function getData() {
  const url = "http://127.0.0.1:5000/scarping_url";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    //console.log(json);
    return json;
  } catch (error) {
    //console.error(error.message);
  }
}

async function logdata() {
  const data = await getData();
  await console.log(data[1].title);
}

logdata();
