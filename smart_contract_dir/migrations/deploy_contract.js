var agentic_smart_contract = artifacts.require("agentic_smart_contract");

module.exports = function(deployer) {
    deployer.deploy(agentic_smart_contract);
};