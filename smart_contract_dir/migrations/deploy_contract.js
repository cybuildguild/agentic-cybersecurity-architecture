const agentic_smart_contract = artifacts.require("agentic_smart_contract");

module.exports = function(deployer) {
    return deployer.deploy(agentic_smart_contract);
};