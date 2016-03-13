# shipEnergyNeutralizerTransferAmountBonusAF
#
# Used by:
# Ship: Cruor
# Ship: Sentinel
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer",
                                  "energyDestabilizationAmount", ship.getModifiedItemAttr("shipBonusAF"), skill="Amarr Frigate")
