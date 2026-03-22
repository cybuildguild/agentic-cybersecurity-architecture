//This will be a logging smart contract
//It will package the actions of the python file agentic_model,
//  and store them


// SPDX-License-Identifier: MIT
pragma solidity >=0.5.0 < 0.9.0;

contract agentic_smart_contract 
{
    // Declare a new complex type which will
    // be used for variables later.
    // It will represent a record of a single 
    // agent's actions.
    struct Record {
        // The following are string types as that is 
        // the return type of those functions in
        // agentic_model.py
        string data;
        string decision;
        string action;
        uint timestamp;
    }

    // Create a dynamically-sized storage array
    Record[] public records;

    function packaging_actions(string calldata _data, string calldata _decision, string calldata _action) public 
    {
        //'Record({...})' creates a temporary Record
        // object and 'records.push(...)' appends
        // it to the end of 'records'.
        records.push(Record({_data, _decision, _action, block.timestamp}));
    }
}