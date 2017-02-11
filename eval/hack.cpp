#include <fstream>      // std::ifstream, std::ofstream

int main () {
		std::ofstream outfile ("newin",std::ofstream::binary);

		outfile.write ("hacked",6);


		outfile.close();
		return 0;
}
