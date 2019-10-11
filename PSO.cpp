#include "AntennaArray.cpp"
#include <random>

std::vector<double> generateValues(AntennaArray array,int arrays){
  int i = 0;
  std::vector<double> values;
  while (i<arrays-1){
    if (i == 0){
      double lowerBound = 0 + array.MIN_SPACING;
      double upperBound = arrays/2;
      double a_random_double = lowerBound + (rand() / ( RAND_MAX / (upperBound-lowerBound) ) ) ;
      values.push_back(a_random_double);
    }
    else{
      int previous = values[i-1];
      double lowerBound = values[previous] + array.MIN_SPACING;
      double upperBound = arrays/2;
      double a_random_double = lowerBound + (rand() / ( RAND_MAX / (upperBound-lowerBound) ) ) ;
      values.push_back(a_random_double);
    }
    i++;
  }
  double final = arrays/2.00;
  values.push_back(final);
  if(array.is_valid(values)){
    return values;
  }
  else{
    std::cout << "Recursive" << '\n';
    return generateValues(array,arrays);
  }
}

void randomSearch(AntennaArray array,int arrays){
  double best = 1000000;
  for (int i =0; i<100;i++){
    std::vector<double> v = generateValues(array,3);
    double current = array.evaluate(v);
    std::cout << current << '\n';
    if(current<best){
      best = current;
    }
  }
  std::cout << best << std::endl;
}

int main(){
  srand((unsigned)time(NULL));
  AntennaArray array(3,90);
  randomSearch(array,3);
  return 0;
}
