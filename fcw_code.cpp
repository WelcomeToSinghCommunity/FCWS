
    // Forward Collision Warning (FCW) System Code (Mock)
    // MISRA-compliant C++ code
    #include <iostream>

    class FCWSystem {
    private:
        float detectionDistance;
        float speedThreshold;

    public:
        FCWSystem(float detection_distance, float speed_threshold)
            : detectionDistance(detection_distance), speedThreshold(speed_threshold) {}

        void detectObstacle(float objectDistance, float objectSpeed) {
            if (objectDistance < detectionDistance && objectSpeed > speedThreshold) {
                std::cout << "Warning: Collision risk detected!" << std::endl;
            } else {
                std::cout << "System status: Safe" << std::endl;
            }
        }
    };

    int main() {
        FCWSystem fcw(50.0, 10.0);  // 50 meters detection distance, 10 m/s speed threshold
        fcw.detectObstacle(30.0, 12.0);  // Example obstacle data
        return 0;
    }
    