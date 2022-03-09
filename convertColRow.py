from csv import reader, writer

ColRow = {
          'start_col': 2, # 開始行
          'start_row': 0, # 開始列
        #   'out_rows': , # 出力列数
         }



def convertColRow(input_csv, start_col, start_row, out_rows=0):
    '''
    csv内の1列に並んでいるデータを指定行×指定列の表に変換する。
    列を指定することで行列数を決定する。（全データ数÷指定列数＝指定行数）
    列数が指定されていない場合、1列に並んでいるデータを1行に変換する。
    '''

    with open(input_csv) as f:
        # 開始行・列からの値をリストに格納
        out_range = [out_row[start_col] for out_row in [row for row in reader(f)][start_row:]]
        # 出力列数が指定されていない場合は1行に変換
        if not out_rows:
            out_rows = len(out_range)
        # 上記リストを出力列数分割
        out_sep = [out_range[idx:idx + out_rows] for idx in range(0,len(out_range), out_rows)]

    with open(f'conved_{input_csv}', 'a') as f:
        # 出力行・列数で出力
        for row in out_sep:
            writer(f, lineterminator='\n').writerow(row)

if __name__ == '__main__':
    convertColRow('input.csv', **ColRow)