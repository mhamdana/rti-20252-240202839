import pandas as pd
from pathlib import Path

files = {
    'Chrome': Path('06-output/Hasil_RAM_Chrome.xlsx'),
    'Chrome_lanjutan': Path('06-output/Hasil_RAM_Chrome_lanjutan.xlsx'),
    'Firefox': Path('06-output/Hasil_RAM_Firefox_5x.xlsx'),
}

for name, path in files.items():
    print('---', name, path, 'exists', path.exists())
    if path.exists():
        df = pd.read_excel(path)
        print('columns', df.columns.tolist())
        if 'Total RAM (MB)' in df.columns:
            s = df['Total RAM (MB)']
            print('n', len(s))
            print('mean', float(s.mean()))
            print('std', float(s.std(ddof=1)))
            print('min', float(s.min()))
            print('25%', float(s.quantile(0.25)))
            print('50%', float(s.median()))
            print('75%', float(s.quantile(0.75)))
            print('max', float(s.max()))
            print(df.head(5).to_string(index=False))
        else:
            print('missing Total RAM (MB) column')
