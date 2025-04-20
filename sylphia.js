
function botActivity(txCount, volume, priceChange) {
  const avgTxVolume = volume / txCount;

  if (txCount > 50 && avgTxVolume < 100 && Math.abs(priceChange) < 1.5) {
    return "Medium Bot Activity";
  } else {
    return "Low Bot Activity";
  }
}

function sybilRisk(txCount) {
  if (txCount > 800) return "High Sybil Risk";
  if (txCount > 300) return "Medium Sybil Risk";
  return "Low Sybil Risk";
}

function whaleActivity(txCount, volume) {
  const avgTxVolume = volume / txCount;

  if (avgTxVolume > 1000 && txCount < 100) return "Accumulation";
  if (avgTxVolume > 1500 && txCount >= 100 && txCount < 200) return "Potential Whale Activity";
  return "Low Whale Activity";
}

const volume = 2000000;
const liquidity = 1500000;
const txCount = 100;
const priceChange = 1.2;

const botActivityResult = botActivity(txCount, volume, priceChange);
const sybilRiskResult = sybilRisk(txCount);
const whaleActivityResult = whaleActivity(txCount, volume);

document.getElementById('botActivityResult').innerHTML = botActivityResult;
document.getElementById('sybilRiskResult').innerHTML = sybilRiskResult;
document.getElementById('whaleActivityResult').innerHTML = whaleActivityResult;
