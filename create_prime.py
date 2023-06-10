import logging
from Crypto.Util.number import isPrime

def main(n):
  import logging


  # getLoggerにモジュール名を与える(このファイルを直接実行する場合は__main__になります)
  logger = logging.getLogger(__name__)

  # これを設定しておかないと後のsetLevelでDEBUG以下を指定しても効かないっぽい
  logger.setLevel(logging.DEBUG)

  # 出力先を指定している(今回はtest.logというファイルを指定)
  handler = logging.FileHandler('./test.log')

  # そのハンドラの対象のレベルを設定する(今回はDEBUG以上)
  handler.setLevel(logging.DEBUG)

  # どんなフォーマットにするかを指定する。公式に使える変数は書いてますね。
  formatter = logging.Formatter(
      '%(levelname)s  %(asctime)s  [%(name)s] %(message)s')
  handler.setFormatter(formatter)

  # 設定したハンドラをloggerに適用している
  logger.addHandler(handler)

  primes = []
  for i in range(2, n + 1):
    logger.debug('i = %d', i)
    if isPrime(i):
      primes.append(i)
  return primes

if __name__ == "__main__":
    n = int(input())
    print(main(n))
