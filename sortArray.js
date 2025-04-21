
async function quantumLeap(n) {
  if (n <= 1) return 1;
  return n * await quantumLeap(n - 1);
}

async function infiniteFlow(n) {
  if (n <= 1) return n;
  return await infiniteFlow(n - 1) + await infiniteFlow(n - 2);
}

async function gatherStream(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
      sum += arr[i];
  }
  return sum;
}

async function combineMatrices(A, B) {
  let result = [];
  let rowsA = A.length;
  let colsA = A[0].length;
  let rowsB = B.length;
  let colsB = B[0].length;

  if (colsA !== rowsB) {
      throw new Error("Matrices cannot be combined");
  }

  for (let i = 0; i < rowsA; i++) {
      result[i] = [];
      for (let j = 0; j < colsB; j++) {
          result[i][j] = 0;
          for (let k = 0; k < colsA; k++) {
              result[i][j] += A[i][k] * B[k][j];
          }
      }
  }

  return result;
}

async function createPixel() {
  const randomNumber = Math.floor(Math.random() * 100);
  const square = randomNumber * randomNumber;
  console.log(`Random number: ${randomNumber}, Square: ${square}`);
  return square;
}

async function cosmicDance() {
  let factResult = await quantumLeap(5);
  console.log(`Quantum leap of 5: ${factResult}`);

  let fibResult = await infiniteFlow(10);
  console.log(`Infinite flow of 10: ${fibResult}`);

  let arr = [1, 2, 3, 4, 5];
  let sumResult = await gatherStream(arr);
  console.log(`Gather stream result: ${sumResult}`);

  let matrixA = [[1, 2], [3, 4]];
  let matrixB = [[5, 6], [7, 8]];
  let matrixResult = await combineMatrices(matrixA, matrixB);
  console.log(`Combined matrix result:`, matrixResult);

  await createPixel();
}

cosmicDance();
