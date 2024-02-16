#!/usr/bin/node
const request = require('request');

// Define the base URL for the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api';

// Function to promisify the request
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

// Function to fetch character names for a given film ID
async function fetchCharacterNames(filmId) {
  try {
    // Fetch film details
    const { body: filmBody } = await promisifiedRequest(`${API_URL}/films/${filmId}/`);
    const film = JSON.parse(filmBody);

    // Extract character URLs from the film details
    const charactersURL = film.characters;

    // Fetch character names concurrently using Promise.all
    const characterNames = await Promise.all(
      charactersURL.map(async (url) => {
        const { body: characterBody } = await promisifiedRequest(url);
        const character = JSON.parse(characterBody);
        return character.name;
      })
    );

    return characterNames;
  } catch (error) {
    // Handle errors and throw a customized error message
    throw new Error(`Error fetching character names: ${error}`);
  }
}

// Main function to execute the script
async function main() {
  try {
    if (process.argv.length > 2) {
      // Extract film ID from command line arguments
      const filmId = process.argv[2];

      // Fetch and display character names
      const characterNames = await fetchCharacterNames(filmId);
      console.log(characterNames.join('\n'));
    } else {
      console.log('Please provide a film ID.');
    }
  } catch (error) {
    // Log any errors that occur during execution
    console.error(error);
  }
}

// Invoke the main function
main();
