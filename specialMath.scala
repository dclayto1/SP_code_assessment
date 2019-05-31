import scala.math.BigInt;
object specialMath {
    // python to scala translated
    def recursiveMath(n: Int) : Int = {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }
        return n + recursiveMath(n-1) + recursiveMath(n-2);
    }

    // looped version so it works for larger numbers
    def loopingMath(n: Int) : BigInt = {
        var current: BigInt = 0;
        var previous: BigInt = 0;
        for(i <- 1 to n) {
            val tmp: BigInt = current;
            current = i + current + previous;
            previous = tmp;
        }
        return current;
    }

    def main(args: Array[String]) {
        if (args.length != 1) {
            println("Invalid usage. Please try: scala specialMath <whole number>");
            System.exit(1);
        }

        try {
            val number: Int = args(0).toInt
            if (number < 0) {
                throw new NumberFormatException;
            }
            println(loopingMath(number));
        } catch {
            case e: NumberFormatException => {
                println(s"The input provided, '${args(0)}', is not a valid whole number.");
                System.exit(1);
            }
        }
    }
}