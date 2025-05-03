// Пример простого смарт-контракта для хранения данных
pragma solidity ^0.8.0;
contract Storage {
    uint256 public data;
    function setData(uint256 _data) public {
        data = _data;
    }
}