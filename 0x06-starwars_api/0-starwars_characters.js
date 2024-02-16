#!/usr/bin/node
const request = require('request');

const API_URL = 'https://swapi-api.hbtn.io/api';

function promisifiedRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function fetchCharacters(movieId) {
  try {
    const { body: movieBody } = await promisifiedRequest(`${API_URL}/films/${movieId}/`);
    const movie = JSON.parse(movieBody);
    const charactersURL = movie.characters;

    for (const url of charactersURL) {
      const { body: characterBody } = await promisifiedRequest(url);
      const character = JSON.parse(characterBody);
      console.log(character.name);
    }
  } catch (error) {
    throw new Error(`Error fetching characters: ${error}`);
  }
}

async function main() {
  try {
    if (process.argv.length > 2) {
      const movieId = process.argv[2];
      await fetchCharacters(movieId);
    } else {
      console.log('Please provide a movie ID.');
    }
  } catch (error) {
    console.error(error.message);
  }
}

main();
