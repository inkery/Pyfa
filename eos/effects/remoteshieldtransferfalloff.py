# remoteShieldTransferFalloff
#
# Used by:
# Modules from group: Remote Shield Booster (31 of 31)
type = "projected", "active"
def handler(fit, container, context):
    if "projected" in context:
        bonus = container.getModifiedItemAttr("shieldBonus")
        duration = container.getModifiedItemAttr("duration") / 1000.0
        fit.extraAttributes.increase("shieldRepair", bonus / duration)
