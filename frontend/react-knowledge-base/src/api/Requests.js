export const GET_REQUEST = async (url) => {
  console.log(url);
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    cache: "no-store",
    credentials: "omit",
    redirect: "follow",
    referrerPolicy: "no-referrer",
  });

  console.log(response);
  if (response.status !== 200) throw new Error("Something went wrong.");

  return await response.json();
};

export const POST_REQUEST = async (url, data) => {
  const response = await fetch(url, {
    method: "POST",
    mode: "cors",
    cache: "no-store",
    credentials: "omit",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(data),
  });

  console.log(response);
  if (response.status !== 200) throw new Error("Something went wrong.");

  return response.json();
};

export const PUT_REQUEST = async (url, data) => {
  const response = await fetch(url, {
    method: "PUT", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-store", // *default, no-cache, reload, force-cache, only-if-cached
    // https://developer.mozilla.org/en-US/docs/Web/API/Request/cache Czy przechowywać dane w pamięci podręcznej
    credentials: "omit", // include, *same-origin, omit
    // https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow", // manual, *follow, error
    // https://developer.mozilla.org/en-US/docs/Web/API/Request/redirect
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });

  console.log(response);
  if (response.status !== 200) throw new Error("Something went wrong.");

  return response.json(); // parses JSON response into native JavaScript objects
};

export const DELETE_REQUEST = async (url) => {
  const response = await fetch(url, {
    method: "GET",
    mode: "cors",
    cache: "no-store",
    credentials: "omit",
    redirect: "follow",
    referrerPolicy: "no-referrer",
  });

  console.log(response);
  if (response.status !== 200) throw new Error("Something went wrong.");

  return response.json();
};
