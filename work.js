const readline = require("readline");

// Configurar la interfaz de readline para leer desde la consola
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Función para mostrar el menú de opciones
function mostrarMenu() {
  return new Promise((resolve) => {
    const menu = `
  --- Menú ---
  1. Ingresar nueva persona
  2. Mostrar todos los datos
  3. Filtrar por DNI
  4. Salir
  Elige una opción:`;

    rl.question(menu, (opcion) => {
      resolve(opcion);
    });
  });
}

// Función para ingresar una nueva persona
function ingresarPersona() {
  return new Promise((resolve) => {
    rl.question("Ingresa el nombre: ", (nombre) => {
      rl.question("Ingresa el apellido: ", (apellido) => {
        rl.question("Ingresa el DNI: ", (dni) => {
          rl.question("Ingresa los teléfonos separados por comas: ", (telefonos) => {
            rl.question("Ingresa los nombres de los hijos separados por comas: ", (hijos) => {
              // Convertir los teléfonos y los hijos a listas
              telefonos = telefonos.split(",").map((t) => t.trim());
              hijos = hijos.split(",").map((h) => h.trim());

              // Crear la persona con la estructura adecuada
              const persona = [nombre, apellido, dni, telefonos, hijos];
              resolve(persona);
            });
          });
        });
      });
    });
  });
}

// Función para mostrar todos los datos de las personas
function mostrarDatos(personas) {
  if (personas.length === 0) {
    console.log("No hay datos para mostrar.");
    return;
  }

  let mensaje = "\nDatos ingresados:";
  personas.forEach((persona) => {
    let [nombre, apellido, dni, telefonos, hijos] = persona;
    mensaje += `\n${nombre} ${apellido}, DNI: ${dni}, Teléfonos: ${telefonos.length} teléfono(s), Hijos: ${hijos.length}`;
  });

  console.log(mensaje);
}

// Función para filtrar personas por DNI
function filtrarPorDni(personas) {
  return new Promise((resolve) => {
    rl.question("Ingresa el DNI para filtrar: ", (dniBuscado) => {
      let personaEncontrada = personas.find((persona) => persona[2] === dniBuscado); // Buscar por DNI

      if (personaEncontrada) {
        let [nombre, apellido, dni, telefonos, hijos] = personaEncontrada;
        console.log(`Datos de ${nombre} ${apellido}:\nDNI: ${dni}, Teléfonos: ${telefonos.length} teléfono(s), Hijos: ${hijos.length}`);
      } else {
        console.log("No se encontró una persona con ese DNI.");
      }

      resolve();
    });
  });
}

// Función principal que controla el flujo del programa
async function main() {
  let personas = []; // Arreglo para almacenar las personas

  while (true) {
    let opcion = await mostrarMenu(); // Mostrar el menú y obtener la opción seleccionada por el usuario

    if (opcion === "1") {
      // Opción 1: Ingresar una nueva persona
      let persona = await ingresarPersona();
      personas.push(persona); // Agregar la persona a la lista
    } else if (opcion === "2") {
      // Opción 2: Mostrar todos los datos
      mostrarDatos(personas);
    } else if (opcion === "3") {
      // Opción 3: Filtrar por DNI
      await filtrarPorDni(personas);
    } else if (opcion === "4") {
      // Opción 4: Salir del programa
      console.log("Gracias por usar el programa.");
      rl.close(); // Cerrar la interfaz de readline
      break; // Terminar el ciclo y salir
    } else {
      // Opción inválida
      console.log("Opción no válida, por favor elige una opción del 1 al 4.");
    }
  }
}

// Iniciar el programa
main();
