def calcular_valor_coluna(merged):
  merged['total_percentual'] = (merged['total'] / merged['total_nivel']) * 100
  return merged