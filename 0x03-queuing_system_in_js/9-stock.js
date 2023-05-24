const listProducts = [{
        id: 1, name: "Suitcase 250", price: 50, stock: 4,
        id: 2, name: "Suitcase 450", price: 100, stock: 10,
        id: 3, name: "Suitcase 650", price: 350, stock: 2,
        id: 4, name: "Suitcase 1050", price: 550, stock: 5
    }];

function getItemById(id) {
    return listProducts.find(item => item.id === id);

}

const express = require('express');
const app = express();
app.listen(1245);

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

const redis = require('redis'),
  client = redis.createClient();
const { promisify } = require('util');

const promisifySet= promisify(client.set).bind(client);
const promisifyGet = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  promisifySet(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  await promisifyGet(`item.${itemId}`);
}

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    getCurrentReservedStockById(itemId).then(stock => {
      item.initialAvailableQuantity = stock;
      res.send(item);
    })
  } else {
    res.status(404).send({ status: 'Product not found' });
  }

app.post('/reserve_products/:itemId/', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (!item) res.status(404).send({ status: 'Product not found' });
  if(item.initialAvailableQuantity < 0) res.status(400).send({ status: 'Not enough stock' });
  else {
      reserveStockById(itemId, item.initialAvailableQuantity - 1);
      res.send({ "status":"Reservation confirmed", "itemId": itemId });
      }
    })
});
