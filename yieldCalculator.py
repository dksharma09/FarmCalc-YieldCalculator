class YieldCalculator:
    def __init__(Self, cropType, areaInAcreasOrHectares, area, expectedYieldPerUnitArea):
        Self.cropType = cropType
        Self.areaInAcreasOrHectares = areaInAcreasOrHectares
        Self.area = int(area)
        Self.expectedYieldPerUnitArea = int(expectedYieldPerUnitArea)
        
    def yieldCalc(Self):
        totalYield = Self.area * Self.expectedYieldPerUnitArea
        return totalYield