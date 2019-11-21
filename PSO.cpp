#include "AntennaArray.cpp"
#include <random>
#include <math.h>

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

class Particle{
public:
  std::vector<double> position;
  std::vector<double> velocity;
  std::vector<double> personalBest;
  double personalBestValue;
  double intertia = 0.721;
  double attraction = 1.1193;

  Particle(AntennaArray array, int arrays){
    position = generateValues(array,arrays);
    std::vector<double> v = generateValues(array,arrays);
    for(int i =0; i<position.size();i+=1){
      velocity.push_back((position[i]-v[i])/2);
    }
    personalBest = position;
    personalBestValue = array.evaluate(personalBest);
  }

  void tick(AntennaArray array, int arrays, std::vector<double> globalBest){
    std::vector<double> newPosition;
    for(int c =0; c<velocity.size();c+=1){
      newPosition.push_back(position[c]+velocity[c]);
    }

    std::vector<double> intertiaVelocity;
    for(int a =0; a<velocity.size();a+=1){
      intertiaVelocity.push_back(velocity[a]*intertia);
    }

    std::vector<double> v;
    for(int i = 0; i<position.size(); i+=1 ){
      v.push_back((personalBest[i]-position[i])*attraction);
    }

    std::vector<double> v2;
    for(int y = 0; y<position.size(); y+=1 ){
      v2.push_back((globalBest[y]-position[y])*attraction);
    }

    std::vector<double> newVelocity;
    for(int b = 0;b<velocity.size();b+=1){
      newVelocity.push_back(intertiaVelocity[b]+v[b]+v2[b]);
    }

    position = newPosition;
    velocity = newVelocity;

    if(array.is_valid(position)){
      double evaluation = array.evaluate(position);
      if(evaluation<personalBestValue){
        personalBest = position;
        personalBestValue = evaluation;
      }
    }
  }
};

class Swarm{
public:
  std::vector<Particle> swarm;
  std::vector<double> globalBest;
  double globalBestValue = 1000000;

  Swarm(AntennaArray array, int arrays){
    int swarmSize = 20 + round(sqrt(arrays));
    for(int i =0; i<swarmSize;i++){
      Particle p(array,arrays);
      swarm.push_back(p);
      if(swarm[i].personalBestValue<globalBestValue){
        globalBest = swarm[i].personalBest;
        globalBestValue = swarm[i].personalBestValue;
      }
    }
  }

  void tick(AntennaArray array, int arrays){
    for(auto& x:swarm){
      x.tick(array,arrays,globalBest);
      if(x.personalBestValue<globalBestValue){
        globalBest=x.personalBest;
        globalBestValue=x.personalBestValue;
      }
    }
  }
};

int main(int argc, char* argv[]){
  srand((unsigned)time(NULL));
  int antennaCount = strtol(argv[1],nullptr,0);
  int angle = strtol(argv[2],nullptr,0);
  AntennaArray array(antennaCount,angle);
  Swarm swarm(array,antennaCount);
  for(int i=0; i<100;i++){
    swarm.tick(array,antennaCount);
  }
  std::cout << "Best value is: " <<swarm.globalBestValue << '\n';
  for(auto const& value: swarm.globalBest){
    std::cout<<value<<std::endl;
  }
  return 0;
}
